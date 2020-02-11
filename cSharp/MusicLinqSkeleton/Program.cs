using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = MusicStore.GetData().AllArtists;
            List<Group> Groups = MusicStore.GetData().AllGroups;

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            // List<Artist> ArtistsFromMV = Artists.Where(art => art.Hometown == "Mount Vernon").ToList();
            List<Artist> ArtistsFromMV = Artists.Where(art => art.Hometown.Contains("Mount Vernon")).ToList();

            //Who is the youngest artist in our collection of artists?
            Artist Youngest = Artists.OrderBy(art => art.Age).FirstOrDefault(); 

            //Display all artists with 'William' somewhere in their real name
            List<Artist> Williams = Artists.Where(art => art.RealName.Contains("William")).ToList();

            //Display the 3 oldest artist from Atlanta
            List<Artist> Oldest = Artists.Where(art => art.Hometown == "Atlanta").OrderByDescending(art => art.Age).Take(3).ToList();

            //(Optional) Display the Group Name of all groups that have members that are not from New York City
            var NotNYC = Groups.Join(Artists, g => g.Id, a => a.GroupId, (group, artist) => group).Where(group => group.Members.All(artist => artist.Hometown != "New York City")).ToList();

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
            List<string> WuTangClan = Artists.Join(Groups, art => art.GroupId, gro => gro.Id, (artist, group) => artist).Where(artist => artist.Group.GroupName == "Wu-Tang Clan").Select(artist => artist.ArtistName).ToList();

	        Console.WriteLine("------------------------------------------------------------------------------------------------------------------------");
	        Console.WriteLine(Groups.Count);
	        Console.WriteLine(Artists.Count);
	        Console.WriteLine("------------------------------------------------------------------------------------------------------------------------");
        }
    }
}
